import CryptoJS from "crypto-js";

// https://medium.com/@sachadehe/encrypt-decrypt-data-between-python-3-and-javascript-true-aes-algorithm-7c4e2fa3a9ff
export const encrypt = (password: string) => {
  var key = process.env.ENCRYPT_KEY || "";
  key = CryptoJS.enc.Utf8.parse(key) as any;

  var iv = CryptoJS.enc.Utf8.parse("UWPMBFUOMDOADSJX");

  var encrypted = CryptoJS.AES.encrypt(password, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
  });
  encrypted = encrypted.toString() as any;
  // console.log("encrypted", encrypted);
  return encrypted;
};
