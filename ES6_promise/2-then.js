export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ body: 'success', status: 200 }))
    .catch(() => new Error())
    .finally(console.log('Got a reponse from the API'));
}
