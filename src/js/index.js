// Global functions
function countWords(s) {
  const word_array = s.replace(/^\s+|\s+$/g,"").split(/\s+/)
  if (word_array.length===1&&word_array[0]==="") return 0
  else return word_array.length
}
function validEmail(email) { // https://stackoverflow.com/a/46181/3006854
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(String(email).toLowerCase())
}

// Stripe purchase
const buyHandler = StripeCheckout.configure({
  key: 'pk_test_absAcyl9d70mNZaoLomaOczZ',
  locale: 'auto',
  zipCode: true,
  token: function(token) {
    // Append token to form
    const form = document.getElementById('translate-form')
    const tokenInput = document.getElementsByName('stripe-token')[0]
    tokenInput.setAttribute('value', token.id)
    form.appendChild(tokenInput)
    form.submit()
  }
})
window.addEventListener('popstate', function() {
  buyHandler.close()
})

// Knockout view model
ko.applyBindings(function() {
  const vm = this
  
  this.submission = ko.observable('')
  this.wordcount = ko.computed(function () {
    return countWords(this.submission())
  })
	this.cost = ko.computed(function() {
	  return (parseInt(this.wordcount(), 10) * document.getElementsByName('price')[0].value).toFixed(2)
	})
	this.pluralWords = ko.computed(function() {
	  return this.wordcount()!==1
	})
	
	// Form submission
  this.formSubmitted = function(formElement) {
    
    emailElement = document.getElementsByName('email')[0]
    submissionElement = document.getElementsByName('submission')[0]
    
    // Make the red boxes normal if validaton failed previously
    submissionElement.style.borderColor = 'initial'
    emailElement.style.borderColor = 'initial'
    
    // Validations
    if (vm.wordcount()===0) {
      alert('The translation of nothing is still nothing...')
      submissionElement.style.borderColor = 'red'
    } else if (emailElement.value==='') {
      alert('Please enter an email address')
      emailElement.style.borderColor = 'red'
    } else if (!validEmail(emailElement.value)) {
      alert('Somethings funny about that email address...')
      emailElement.style.borderColor = 'red'
    }
    
    // All valid, open purchase popup
    else buyHandler.open({
	    name: 'Translation',
	    description: 'Translation of '+vm.wordcount().toString()+' words into English',
	    email: emailElement.value,
	    amount: vm.cost()*100,
  	})
  
  }
	
})
