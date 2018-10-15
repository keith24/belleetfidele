// Global vars
const xhr = new XMLHttpRequest()

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
  
    // POST the data!
    xhr.open('POST', 'https://formspree.io/translate@ki9.us')
    xhr.send({
      'token': token.id,
      'email': document.getElementById('email').value,
      'submission': document.getElementById('submission').value,
      'wordcount': document.getElementById('wordcount').innerHTML,
      'cost': document.getElementById('cost').innerHTML,
    })
    
    // And clear that form! 
	  document.getElementById('email').value = ''
	  document.getElementById('submission').value = ''
	  document.getElementById('wordcount').innerHTML = '0'
	  
  }
})

// Form submission
document.getElementById('buy-btn').addEventListener('click', function(e) {
  
  // TODO: Make the red boxes normal again
  
  email = document.getElementById('email').value
  wordcount = document.getElementById('wordcount').innerHTML
  cost = document.getElementById('cost').innerHTML
  
  // Validations
  if (wordcount==0) {
    alert('The translation of nothing is still nothing...')
    //TODO: Make submission box red or whatever
  } else if (email==='') {
    alert('Please enter an email address')
    //TODO: Make email box red or whatever
  } else if (!validEmail(email)) {
    alert('Somethings funny about that email address...')
    //TODO: Make email box red or whatever
  }
  
  // All valid, open purchase popup
  else buyHandler.open({
	  name: 'Translation',
	  description: 'Translation of '+wordcount+' words into English',
	  email: email,
	  amount: parseFloat(cost)*100,
	})
  
})
// Stripe wants this to be included
window.addEventListener('popstate', function() {
  buyHandler.close()
})

// https://stackoverflow.com/a/46181/3006854
function validEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(String(email).toLowerCase());
}
