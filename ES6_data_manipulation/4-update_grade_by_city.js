export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const filteredStudents = studentList.filter(
    (student) => student.location === city,
  );

  const updatedStudents = filteredStudents.map((student) => {
    const matchingGrade = newGrades.find(
      (grade) => grade.studentId === student.id,
    );

    return { ...student, grade: matchingGrade ? matchingGrade.grade : 'N/A' };
  });

  return updatedStudents;
}
