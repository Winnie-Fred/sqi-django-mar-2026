const newsletterDiv = document.getElementById("newsletterPopUp");

setTimeout(() => {
  newsletterDiv.style.display = "flex";
}, 2000);

const closeBtn = document.getElementById("closeBtn");

closeBtn.addEventListener("click", function() {
  newsletterDiv.style.display = "none";
})