export default class CommonUtils {
  constructor() {}
  static validatePhoneNumber(number) {
    let phoneno = /^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/;
    return number.match(phoneno)
  }
}
