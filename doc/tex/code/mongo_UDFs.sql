//extract bedrooms
db.zillow.aggregate([
	  {
	    $project: {
	      returnObject: {
	        $regexFindAll: { input: "$facts and features", regex: /\S+(?= bds)/ }
		      }
		    }
		  }
		])

	//bathrooms
	db.zillow.aggregate([
		  {
		    $project: {
		      returnObject: {
		        $regexFindAll: { input: "$facts and features", regex: /\S+(?= ba)/ }
			      }
			    }
			  }
			])

		//sqft
		db.zillow.aggregate([
			  {
			    $project: {
			      returnObject: {
			        $regexFindAll: { input: "$facts and features", regex: /\S+(?= sqft)/ }
				      }
				    }
				  }
				])
