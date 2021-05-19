var message = "Hello Apple Appricote";
console.log(message);
var Greeting = /** @class */ (function () {
    function Greeting() {
    }
    Greeting.prototype.greet = function () {
        console.log('Hello :)');
    };
    return Greeting;
}());
var obj = new Greeting();
obj.greet();
var str = '1';
var str2 = str;
console.log(typeof (str2));
