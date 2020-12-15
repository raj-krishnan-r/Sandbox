const  aesjs = require('aes-js');
const pkcs7 = require('pkcs7');
 var key = [ 83, 84, 79, 80, 82, 69, 65, 68, 77, 79, 86, 69, 83, 84, 79, 80 ];
 var iv = [ 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83,83, 83 ];
const en=(text)=>{
var textBytes = pkcs7.pad(aesjs.utils.utf8.toBytes(text));
var aesCbc = new aesjs.ModeOfOperation.cbc(key,iv)
var encryptedBytes = aesCbc.encrypt(textBytes);
var encryptedHex = aesjs.utils.hex.fromBytes(encryptedBytes);
return encryptedHex;
}


const de=(text)=>{
var hexDecrypt = aesjs.utils.hex.toBytes(text);
var aesCbc = new aesjs.ModeOfOperation.cbc(key,iv);
var decryptedText = aesCbc.decrypt(hexDecrypt);
var op = aesjs.utils.utf8.fromBytes(pkcs7.unpad(decryptedText));
return op;
}
