def get_internship():
	title = input("Internship title: ")
	company = input("Company name: ")
	location = input("Location: ")
	rating = int(input("Rating (1-10): "))
	
	return{
	"title": title,
	"company": company,
	"location": location,
	"rating": rating
	}

internships = []

for i in range(3):
	print(f"Internship #{i+1}")
	internship = get_internship()
	internships.append(internship)
print(f"All internships: ")
for i in internships:
	print(f"{i['title']} at {i['company']} in {i['location']} - Rated {i['rating']}/10")
