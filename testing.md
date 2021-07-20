# Testing

## Contents

- [Validator Testing](#validator-testing)
- [LightHouse Testing](#lighthouse-testing)
- [Testing for user strories](#testing-for-user-stories)
- [Manually Testing](#manually-testing)
- [Responsiveness Testing](#responsiveness-testing)
- [Bugs and solutions](#bugs-and-solutions)

## **Validator Testing**

### **HTML**

I used [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/) to test my html code.

Because the code is written using Jinja templates, I had to use "view page source" code by right clicking each live page, and run that code through the validator.

I got the following errors :

![error1](static/documentation/html-error1.png)
I fixed this error by replace the `<span>` element with li, and add custom css to style it.

![error2](static/documentation/html-error2.png)
I fixed this error by adding an alt attribute to all `<img>` element.
![error3](static/documentation/html-error3.png)

This is an error due to Jinjia templates, the loop caused duplicated id.

### **CSS**

I have used the W3C CSS Validation Service to validate my CSS code. An error was found see below. ⬇️

![css-error](static/documentation/css-error.png)

I fixed this error by using margin instead of margin-block.

The result came back clear! ⬇️

![css-no-error](static/documentation/css-no-error.png)

### **Javascript**

I used [JSHint](https://jshint.com/) to validate my Javascript code. I have got three unused variables, see the error message below. ⬇️

![js-error](static/documentation/js-error.png)

I checked them, `input`are unnessary, so I deleted it.

The "goBack" function are used in HTML as onlick method. See below ⬇️

![js-error-explained](static/documentation/js-error-explained2.png)

The same issue for the creatInput function, it has been called in HTML code. See below ⬇️

![js-error-explained](static/documentation/js-error-explained1.png)

### **Python**

I checked my app.py file using [PEP8 online](http://pep8online.com/checkresult), errors shows below ⬇️

![py-error](static/documentation/py-error.png)

In order to fix the errors, I had to disable Pylance.

## **LightHouse Testing**

After validating all codes, I ran the site through Chrome LightHouse. The initial scores were below: ⬇️

![LightHouse Report](static/documentation/lighthouse-report1.png)

Taking the feedback into account, I have looked into the recommedations and will bear it in mind for future project.
