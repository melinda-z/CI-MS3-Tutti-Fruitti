// materilize initialization
$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".slider").slider();
  $("select").formSelect();
});
// Add ingredient functionality
var add = document.getElementById("add");
var input = document.getElementById("new-ingredient");
var ul = document.getElementById("ingredients-list");

function inputLength() {
  return input.value.length;
}

function createInput() {
  var newInput = document.createElement("input");
  newInput.setAttribute("type", "text");
  newInput.setAttribute("name", "new-ingredient");
  newInput.setAttribute("minlength", "5");
  newInput.setAttribute("maxlength", "50");
  newInput.setAttribute("placeholder", "Enter Your Ingredient");
  newInput.setAttribute("class", "col");
  newInput.setAttribute("class", "s8");
  var deleteButton = document.createElement("button");
  var t = document.createTextNode("Delete");
  deleteButton.appendChild(t);
  ul.appendChild(newInput);
  ul.appendChild(deleteButton);
  function deleteInput() {
    newInput.remove();
    deleteButton.remove();
  }
  deleteButton.addEventListener("click", deleteInput);
}

// function createListElement() {
//   var li = document.createElement("li");
//   li.appendChild(document.createTextNode(input.value));
//   ul.appendChild(li);
//   input.value = "";
//   var deleteButton = document.createElement("button");
//   deleteButton.style.marginLeft = "60px";
//   deleteButton.style.backgroundColor = "#81c784";
//   deleteButton.style.borderRadius = "5px";
//   deleteButton.className = "b";

//   var buttonText = document.createTextNode("Delete");
//   deleteButton.appendChild(buttonText);
//   li.appendChild(deleteButton);
//   function deleteItems() {
//     li.remove();
//   }
//   deleteButton.addEventListener("click", deleteItems);
// }
function addListAfterClick() {
  if (inputLength() > 0) {
    createInput();
  }
}

function addListAfterKeypress(event) {
  if (inputLength() > 0 && event.keyCode === 13) {
    createInput();
  }
}
add.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress);
