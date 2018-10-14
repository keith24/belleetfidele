ko.applyBindings(function() {
  this.submission = ko.observable('')
  this.wordcount = ko.computed(function () {
    return countWords(this.submission())
  })
	this.price = ko.computed(function() {
	  return (parseInt(this.wordcount(), 10) * .3).toFixed(2)
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
