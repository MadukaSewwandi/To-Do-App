TC ID	Test Case Description	    Precondition	Steps	                            Expected Result	                  Status
TC01	Verify UI loads correctly	App running	    Open app in browser	                UI loads with title, input, and Abutton	                                                                                                                                                                    Pass
TC02	Verify adding a new task	App running	    Enter task & click Add	            Task added to list	                Pass
TC03	Prevent empty task	        App running	    Click Add without entering task	    Error message or nothing added	    Pass
TC04	Edit a task	                Task exists	    Click edit icon, modify text, save	Task updated	                    Pass
TC05	Delete a task	            Task exists	    Click delete icon	                Task removed	                    Pass
TC06	UI responsiveness	        App open	    Resize screen	                    UI adjusts without break	        Pass
TC07	Duplicate task behavior	    App running	    Add same text twice	                Both or validation	                Pass
