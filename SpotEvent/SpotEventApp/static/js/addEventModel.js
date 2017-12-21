var viewModel = new function()
{
    var self = this;
    
    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

    self.event = {
    	venue_id : ko.observable(),
    	user_id : ko.observable('http://127.0.0.1:8000/api/user/' + '1'),
    	event_name : ko.observable('Robin'),
    	event_date : ko.observable('2017-11-11'),
    	artists : ko.observable('Robin'),
    	genre : ko.observable('Rock'),
    }

    self.venue = {
    	venue_name : ko.observable('Robin'),
    	street : ko.observable('Robin'),
    	number : ko.observable('27'),
    	zip_code : ko.observable('1730'),
    	city : ko.observable('Asse'),
    	country : ko.observable('Belgium'),
    }

    self.addEvent = function(){
    	var Json = $.post('/api/venue', ko.toJS(self.venue),function(data){
    		self.event.venue_id('http://127.0.0.1:8000/api/venue/' + data.id);
    		console.log('Event :',data)
    		var Json2 = $.post('/api/event', ko.toJS(self.event));
    	});
    	
    };
    
};

ko.applyBindings(viewModel);  