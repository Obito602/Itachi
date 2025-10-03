main=document.getElementById("main");
let arr=["https://i.pinimg.com/236x/c3/b3/f1/c3b3f1ea25dbf06e84b214751667cbee.jpg",
     "https://i.pinimg.com/236x/5d/6d/23/5d6d23fd7adb44baba20a60c252da339.jpg",
 "https://i.pinimg.com/236x/9c/22/88/9c2288407d7048fbb73e4a736dc4306d.jpg"
 ,"https://i.pinimg.com/564x/a9/df/1f/a9df1f615a20823dd4400c27bdeac688.jpg",
"img2/ch1.jpeg","img2/dr.jpeg" ,"img2/b.jpeg" ,"img2/pic.jpeg",
]
let s="";
for(let i=1;i<=65; i++){
    let r=Math.floor(Math.random()*arr.length)
    s+=`<div class="card"><img src="${arr[r]}"></div>`;
}
main.innerHTML= s;