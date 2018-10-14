ko.applyBindings(function() {
  this.submission = ko.observable('')
  this.wordcount = ko.computed(function () {
    return countWords(this.submission())
  })
	this.cost = ko.computed(function() {
	  return (parseInt(this.wordcount(), 10) * document.getElementById('price').value).toFixed(2)
	})
	this.pluralWords = ko.computed(function() {
	  return this.wordcount()!==1
	})
})

function countWords(s) {
  const word_array = s.replace(/^\s+|\s+$/g,"").split(/\s+/)
  if (word_array.length===1&&word_array[0]==="") return 0
  else return word_array.length
}

const buyHandler = StripeCheckout.configure({
  key: 'pk_test_absAcyl9d70mNZaoLomaOczZ',
  locale: 'auto',
  token: function(token) {
  	console.log(token.id)
    // TODO: Send token ID, and text to my email
  }
})
document.getElementById('buy-btn').addEventListener('click', function(e) {
  buyHandler.open({
    name: 'Translation',
    description: 'Translation of '+document.getElementById('wordcount').innerHTML+' words into English',
    email: document.getElementById('buyer-email').value,
    amount: parseFloat(document.getElementById('cost').innerHTML)*100,
  })
  e.preventDefault()
})
window.addEventListener('popstate', function() {
  buyHandler.close()
});