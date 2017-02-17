window.onload = function () {
  var request = superagent
  var submit = document.getElementById('submit')
  var image = document.getElementById('lovesome')
  var re = /^[A-Z0-9]{1}$/
  console.log(image.src)
  submit.addEventListener('click', function () {
    var
      word2 = document.getElementsByName('word2')[0].value,
      word3 = document.getElementsByName('word3')[0].value
    if (!word2.match(re) || !word3.match(re)) {
      alert('只能输入一个大写英文字母!')
      return
    }
    request
      .get('./draw')
      .query({ word2: word2 })
      .query({ word3: word3 })
      .end(function (err, res) {
        if (res.body.message === 'ok') {
          console.log('success')
          image.src = './static/' + 'I' + word2 + word3 + '.jpg'
        }
      });
  })


}