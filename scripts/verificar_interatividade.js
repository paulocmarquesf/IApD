/* Teste de inicialização sem navegador: detecta exceções de JavaScript e regressões. */
const fs=require('fs'),path=require('path'),vm=require('vm');
const root=path.resolve(__dirname,'..');
let tests=0,errors=[];
function fakeEnv(n){
 const nodes={},values={c:'a',x:'8',y:'6',m:'Meu pedido P0531 está atrasado.',v:'base',w:'50',step:'1',k:'3',hist:'rate',model:'A',mode:'all',case:'5',ap:'no',p:'90'};
 for(const name of ['sim-root','result',...Object.keys(values),'vx','vy','wval','pval','kval','run'])nodes[name]={value:values[name]||'',innerHTML:'',textContent:'',onchange:null,oninput:null,onclick:null};
 const document={body:{dataset:{lesson:String(n)}},readyState:'complete',getElementById:k=>nodes[k]|| (nodes[k]={innerHTML:'',value:'',textContent:''})};
 return {nodes,context:{document,console,Number,Math,JSON,Date,String,Array,Object}};
}
let sim=fs.readFileSync(path.join(root,'docs/assets/javascripts/simulator.js'),'utf8');
for(let n=1;n<=12;n++){
 try{let {context,nodes}=fakeEnv(n);vm.runInNewContext(sim,context,{filename:'simulator.js'});if(!nodes.result.innerHTML)throw Error('Sem saída');tests++;}
 catch(e){errors.push(`Simulador ${n}: ${e.message}`)}
}
const quiz=fs.readFileSync(path.join(root,'docs/assets/javascripts/quiz.js'),'utf8');
(async()=>{
 for(let n=1;n<=12;n++){
  try{
   const src=path.join(root,'docs/assets/quizzes',String(n).padStart(2,'0')+'-conceitos.json');
   const el={dataset:{},innerHTML:'',getAttribute:k=>k==='data-quiz-src'?'mock':null,querySelector:k=>k==='button'?btn:null};
   const btn={onclick:null};
   const document={readyState:'complete',querySelectorAll:()=>[el]};
   const fetch=async()=>({ok:true,json:async()=>JSON.parse(fs.readFileSync(src,'utf8'))});
   vm.runInNewContext(quiz,{document,fetch,console,Number,String,Math,JSON},{filename:'quiz.js'});
   await new Promise(resolve=>setTimeout(resolve,0));
   if(!el.innerHTML.includes('Conferir respostas')||typeof btn.onclick!=='function')throw Error('Quiz não carregou');
   tests++;
  }catch(e){errors.push(`Quiz ${n}: ${e.message}`)}
 }
 console.log(`Testes de inicialização JS: ${tests}; falhas: ${errors.length}`);
 for(const e of errors)console.error(e);
 if(errors.length)process.exit(1);
})();
