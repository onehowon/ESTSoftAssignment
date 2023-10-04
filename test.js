fetch('http://localhost:3001/product', {
  method: 'GET'
})
.then((response) => response.json())
.then((data) => {
  console.log('성공:', data);
})
.catch((error) => {
  console.error('실패:', error);
});