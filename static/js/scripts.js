$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".slider").slider();
  $("select").formSelect();
});

var add = document.getElementById("add");
var input = document.getElementById("new-ingredient");
var ul = document.getElementById("ingredients-list");
var li = document.querySelectorAll("li");

function inputLength() {
  return input.value.length;
}

function createListElement() {
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(input.value));
  console.log(input.value);
  ul.appendChild(li);
  input.value = "";
  var deleteButton = document.createElement("button");
  var buttonText = document.createTextNode("Delete");
  deleteButton.appendChild(buttonText);
  li.appendChild(deleteButton);
  function deleteItems() {
    li.remove();
  }
  deleteButton.addEventListener("click", deleteItems);
}
function addListAfterClick() {
  if (inputLength() > 0) {
    createListElement();
  }
}

function addListAfterKeypress(event) {
  if (inputLength() > 0 && event.keyCode === 13) {
    createListElement();
  }
}
add.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress);
