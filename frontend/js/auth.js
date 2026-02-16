const container = document.getElementById("container");
const signupBtn = document.getElementById("signup");
const loginBtn = document.getElementById("login");

if(signupBtn){
  signupBtn.addEventListener("click", () => {
    container.classList.add("active");
  });
}

if(loginBtn){
  loginBtn.addEventListener("click", () => {
    container.classList.remove("active");
  });
}
