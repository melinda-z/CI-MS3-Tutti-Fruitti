// materilize initialization
$(document).ready(function () {
  $(".sidenav").sidenav({ edge: "right" });
  $(".slider").slider();
  $("select").formSelect();
  // fix materilize form validation issue
  validateMaterializeSelect();
  function validateMaterializeSelect() {
    let classValid = {
      "border-bottom": "1px solid #4caf50",
      "box-shadow": "0 1px 0 0 #4caf50",
    };
    let classInvalid = {
      "border-bottom": "1px solid #f44336",
      "box-shadow": "0 1px 0 0 #f44336",
    };
    if ($("select.validate").prop("required")) {
      $("select.validate").css({
        display: "block",
        height: "0",
        padding: "0",
        width: "0",
        position: "absolute",
      });
    }
    $(".select-wrapper input.select-dropdown")
      .on("focusin", function () {
        $(this)
          .parent(".select-wrapper")
          .on("change", function () {
            if (
              $(this)
                .children("ul")
                .children("li.selected:not(.disabled)")
                .on("click", function () {})
            ) {
              $(this).children("input").css(classValid);
            }
          });
      })
      .on("click", function () {
        if (
          $(this)
            .parent(".select-wrapper")
            .children("ul")
            .children("li.selected:not(.disabled)")
            .css("background-color") === "rgba(0, 0, 0, 0.03)"
        ) {
          $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
          $(".select-wrapper input.select-dropdown").on(
            "focusout",
            function () {
              if (
                $(this)
                  .parent(".select-wrapper")
                  .children("select")
                  .prop("required")
              ) {
                if (
                  $(this).css("border-bottom") != "1px solid rgb(76, 175, 80)"
                ) {
                  $(this)
                    .parent(".select-wrapper")
                    .children("input")
                    .css(classInvalid);
                }
              }
            }
          );
        }
      });
  }
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
  deleteButton.setAttribute("class", "btn-small");
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
