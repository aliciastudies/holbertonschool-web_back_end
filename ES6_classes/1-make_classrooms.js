import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classSize = [19, 20, 34];
  const rooms = [];
  for (const size of classSize) {
    const newRoom = new ClassRoom(size);
    rooms.push(newRoom);
  }
  return rooms;
}
