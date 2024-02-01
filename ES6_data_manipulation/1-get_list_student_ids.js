export default function getListStudentIds(arrayObjs) {
  if (!Array.isArray(arrayObjs)) {
    return [];
  }
  return arrayObjs.map((x) => x.id);
}
