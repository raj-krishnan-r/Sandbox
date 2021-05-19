var message:string = "Hello Apple Appricote"
console.log(message)

class Greeting{
    greet(): void{
        console.log('Hello :)')
    }
}

var obj = new Greeting();
obj.greet()

var str = '1'
var str2:number = <number> <any> str
console.log(typeof(str2))