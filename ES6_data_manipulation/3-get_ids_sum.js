export default function getStudentIdsSum(students) {
  const sumIds = students.reduce((accumulator, x) => accumulator + x.id, 0);
  return sumIds;
}
