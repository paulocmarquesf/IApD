(function(){'use strict';
const AUTH='course_insper_auth_v1',U='inspirar',P='pertencer';
function unlock(){document.body.classList.add('course-authorized');const g=document.getElementById('course-gate');if(g)g.remove();}
function main(){
 if(sessionStorage.getItem(AUTH)==='ok'){unlock();return;}
 const root=document.createElement('div');root.id='course-gate';root.className='course-gate';root.setAttribute('role','dialog');root.setAttribute('aria-modal','true');root.setAttribute('aria-label','Acesso ao curso');
 const origin=(document.querySelector('meta[name="course-asset-root"]')||{}).content||'';
 root.innerHTML='<section class="course-gate__box"><img class="course-gate__logo" alt="Insper" src="'+origin+'assets/images/insper-logo.png"><h1>Inteligência Artificial para Decisão</h1><p>Material da disciplina · Insper</p><form id="course-login"><label for="course-user">Usuário</label><input id="course-user" name="username" autocomplete="username" required><label for="course-pass">Senha</label><input id="course-pass" type="password" name="password" autocomplete="current-password" required><button type="submit">Acessar o curso</button><p class="error" id="course-err" role="alert" aria-live="polite"></p></form></section>';
 document.body.appendChild(root);
 root.querySelector('#course-login').addEventListener('submit',function(e){e.preventDefault();const u=root.querySelector('#course-user').value.trim(),p=root.querySelector('#course-pass').value;if(u===U&&p===P){sessionStorage.setItem(AUTH,'ok');unlock();}else{root.querySelector('#course-err').textContent='Usuário ou senha incorretos.';root.querySelector('#course-pass').value='';root.querySelector('#course-pass').focus();}});
 root.querySelector('#course-user').focus();
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',main);else main();
})();