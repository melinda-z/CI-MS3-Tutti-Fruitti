// materilize initialization
$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".slider").slider();
  $("select").formSelect();
});

// Add ingredient input functionality
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

function addListAfterClick() {
  if (inputLength() > 0) {
    createInput();
  }
}

add.addEventListener("click", addListAfterClick);
