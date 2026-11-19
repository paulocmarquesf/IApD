const fs=require('fs'),path=require('path'),vm=require('vm');
const js=fs.readFileSync(path.resolve(__dirname,'../docs/assets/javascripts/gate.js'),'utf8');
const store=new Map();let gateNode=null,authorized=false,submitted=null;
const fields={
 '#course-user':{value:'',focus(){},},
 '#course-pass':{value:'',focus(){}},
 '#course-err':{textContent:''},
 '#course-login':{addEventListener(name,fn){if(name==='submit')submitted=fn}}
};
const root={innerHTML:'',id:'',className:'',setAttribute(){},querySelector(k){return fields[k]},remove(){gateNode=null}};
const document={readyState:'complete',body:{classList:{add(k){authorized=k==='course-authorized'}},appendChild(x){gateNode=x}},createElement(){return root},getElementById(k){return k==='course-gate'?gateNode:null},querySelector(){return {content:'./'}}};
const sessionStorage={getItem:k=>store.get(k),setItem:(k,v)=>store.set(k,v)};
vm.runInNewContext(js,{document,sessionStorage,console},{filename:'gate.js'});
if(!gateNode||authorized||typeof submitted!=='function')throw Error('Gate não foi exibido');
fields['#course-user'].value='inspirar';fields['#course-pass'].value='errada';submitted({preventDefault(){}});
if(!gateNode||authorized||!fields['#course-err'].textContent)throw Error('Senha incorreta foi aceita');
fields['#course-user'].value='inspirar';fields['#course-pass'].value='pertencer';submitted({preventDefault(){}});
if(gateNode||!authorized||store.get('course_insper_auth_v1')!=='ok')throw Error('Autenticação correta falhou');
console.log('Gate JS: rejeição de senha errada, login correto e sessão validados');
