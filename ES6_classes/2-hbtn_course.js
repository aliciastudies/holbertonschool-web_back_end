export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string.');
    } else {
      this._name = value;
    }
  }

  get name() {
    return this._name;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw TypeError('Length must be a number.');
    } else {
      this._length = value;
    }
  }

  get length() {
    return this._length;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw TypeError('Students must be an array.');
    } else {
      this._students = value;
    }
  }

  get students() {
    return this._students;
  }
}
