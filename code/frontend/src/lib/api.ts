const API=import.meta.env.VITE_API_URL??'http://localhost:8000';
export async function request<T=any>(path:string,token:string,options:RequestInit={}):Promise<T>{
 const r=await fetch(API+path,{...options,headers:{'Content-Type':'application/json',...(token?{Authorization:'Bearer '+token}:{}),...(options.headers||{})}});
 if(!r.ok) throw new Error((await r.json().catch(()=>({detail:'Request failed'}))).detail||'Request failed');
 return r.status===204?null as T:r.json();
}
export const apiBase=API;
