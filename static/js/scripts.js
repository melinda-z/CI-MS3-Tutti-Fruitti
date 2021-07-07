// materilize initialization
$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".slider").slider();
  $("select").formSelect();
});

// Add ingredient input functionality
const add = document.getElementById("add");
const input = document.getElementById("new-ingredient");
const ingredientList = document.getElementById("ingredients-list");

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
  ingredientList.appendChild(newInput);
  ingredientList.appendChild(deleteButton);
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

// Add method steps functionality
const addSteps = document.getElementById("add-steps");
const methodInput = document.getElementById("method");
const stepList = document.getElementById("step-list");

function methodInputLength() {
  return methodInput.value.length;
}

function createTextArea() {
  var newMethodInput = document.createElement("textarea");
  newMethodInput.setAttribute("type", "text");
  newMethodInput.setAttribute("class", "materialize-textarea");
  newMethodInput.setAttribute("name", "method");
  newMethodInput.setAttribute("minlength", "5");
  newMethodInput.setAttribute("maxlength", "250");
  newMethodInput.setAttribute("placeholder", "Add steps");
  var deleteButton = document.createElement("button");
  var t = document.createTextNode("Delete");
  deleteButton.appendChild(t);
  stepList.appendChild(newMethodInput);
  stepList.appendChild(deleteButton);
  function deleteInput() {
    newMethodInput.remove();
    deleteButton.remove();
  }
  deleteButton.addEventListener("click", deleteInput);
}
function addMethodListAfterClick() {
  if (methodInputLength() > 0) {
    createTextArea();
  }
}

addSteps.addEventListener("click", addMethodListAfterClick);
