ko.applyBindings(function() {
  this.submission = ko.observable('')
  this.wordcount = ko.computed(function() {
  	return this.submission().split(' ').length
	})
	this.price = ko.computed(function() {
	  return parseInt(this.wordcount(), 10) * 3
	})
})
