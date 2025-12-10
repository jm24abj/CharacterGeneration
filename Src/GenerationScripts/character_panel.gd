extends Panel

const ALL_NAMES: Array[String] = [
	"Alice", "Benjamin", "Chloe", "Daniel", "Emma",
	"Finn", "Grace", "Henry", "Isla", "Jack",
	"Lily", "Mason", "Nora", "Oliver", "Poppy",
	"Quinn", "Ruby", "Samuel", "Tara", "Uma",
	"Violet", "William", "Xavier", "Yara", "Zoe"
]

var ALL_ATTRIBUTES: Array[String] = [
	"Strength", "Athletics", "Construction",
	"Digging", "Learning", "Medicine", "Cuisine", 
	"Creativity", "Machinery", "Ranching", "Tidying"
]

var ALL_GOOD_TRAITS: Array[String] = [
	"Buff", "Decreased Air Consumption Rate", "Decreased Decor Expectation",
	"Decreased Bladder", "Divers Lung", "Early Bird", "Farmer's Touch",
	"Germ Resistant", "Greasemonkey", "Green Thumb", "Increased Athletics",
	"Increased Bladder", "Increased Machinery", "Increased Strength", "Increased Science",
	"Iron Gut", "Light Eater", "Night Owl", "Quick Learner", "Twinkletoes"
]

var ALL_BAD_TRAITS: Array[String] = [
	"Allergies", "Anemic", "Bottomless Stomach", "Building Disabled",
	"Can't Research", "Cuisine Disabled", "Decreased Athletics", "Decreased Machinery",
	"Decreased Science", "Decreased Strength", "Flatulent", "Increased Air Consumption Rate",
	"Increased Decor Expectation", "Loud Sleeper", "Mouth Breather", 
	"Narcoleptic", "Pacifist", "Small Bladder",
	"Slow Learner", "Snorer", "Squeamish", "Supplying Disabled",
	"Uncultured", "Yokel", "None"
]


var ALL_OVERJOYED_RESPONSES: Array[String] = [
	"Balloon Artist", "Candy Distributor", "Chore Speed",
	"Creative", "Dance", "Hug", "Sparkle Streaker"
]

var ALL_STRESS_REACTIONS: Array[String] = [
	"Binge Eater", "Destructive", 
	"Ugliest Crier", "Vomiter"
]

# useful labels
@onready
var characterNameLabel : Label = $CharacterLayout/TitleHolder/MarginContainer/HBoxContainer/Label
@onready
var characterImage : TextureRect = $CharacterLayout/Stats/CharacterLayout2/AttributesHolder/CharacterImage
@onready
var goodAttributesLabel : RichTextLabel = $CharacterLayout/Stats/CharacterLayout2/AttributesHolder/VBoxContainer/HBoxContainer/Pros
@onready
var badAttributesLabel : RichTextLabel = $CharacterLayout/Stats/CharacterLayout2/AttributesHolder/VBoxContainer/HBoxContainer/Cons
@onready
var goodTraitsLabel : RichTextLabel = $CharacterLayout/Stats/CharacterLayout2/TraitsHolder/HBoxContainer/Pros
@onready
var badTraitsLabel : RichTextLabel = $CharacterLayout/Stats/CharacterLayout2/TraitsHolder/HBoxContainer/Cons
@onready
var characterResponsesLabel : RichTextLabel = $CharacterLayout/Stats/CharacterLayout2/ExtraHolder/HBoxContainer/Responses

# Called when the node enters the scene tree for the first time.
func _ready():
	rollCharacter()

func rollName():
	characterNameLabel.text = ALL_NAMES[randi_range(0,ALL_NAMES.size()-1)]
	
func rollAttributes():
	const MAX_ATTRIBUTES : int = 7
	const MAX_POINTS_COUNT : int = 11
	var assignedPoints : int = 0
	
	goodAttributesLabel.clear()
	goodAttributesLabel.text = ""
	badAttributesLabel.clear()
	goodAttributesLabel.text = ""
	
	var numOfDebuffs : int = 0
	var attributesAdded : int = 0
	
	while (assignedPoints < MAX_POINTS_COUNT) and (attributesAdded < MAX_ATTRIBUTES):
		var isDebuff : bool = randi_range(1,4 + (numOfDebuffs * 2)) == 1
		var attribute : String = ALL_ATTRIBUTES[randi_range(0,ALL_ATTRIBUTES.size()-1)]
		var value : int = randi_range(1,MAX_POINTS_COUNT-assignedPoints)
		
		if isDebuff:
			numOfDebuffs += 1
			assignedPoints -= value
			badAttributesLabel.add_text(" -" + str(value) + " " + attribute + "\n")
		else:
			assignedPoints += value
			goodAttributesLabel.add_text(" +" + str(value) + " " + attribute + "\n")
		
		attributesAdded +=1
		
func rollTraits():
	const MAX_TRAIT_COUNT : int = 4
	var traitCount : int = randi_range(1,MAX_TRAIT_COUNT)
	
	goodTraitsLabel.clear()
	badTraitsLabel.clear()
	
	goodTraitsLabel.text = ""
	badTraitsLabel.text = ""
	
	var goodTrait : int
	
	var hasGoodTraits: bool = false
	var hasBadTraits: bool = false

	for i in range(traitCount):
		goodTrait = randi_range(0,1)
		if goodTrait == 1:
			hasGoodTraits = true
			goodTraitsLabel.add_text(". " + ALL_GOOD_TRAITS[randi_range(0,ALL_GOOD_TRAITS.size()-1)])
			goodTraitsLabel.add_text("\n")
		else:
			hasBadTraits = true
			badTraitsLabel.add_text(". " + ALL_BAD_TRAITS[randi_range(0,ALL_BAD_TRAITS.size()-1)])
			badTraitsLabel.add_text("\n")
	
	if not hasBadTraits:
		badTraitsLabel.text = "N/A"
	if not hasGoodTraits:
		goodTraitsLabel.text = "N/A"
		
func rollResponses():
	var responses : Array[String] = []
	responses.append(ALL_STRESS_REACTIONS[randi_range(0,ALL_STRESS_REACTIONS.size()-1)])
	responses.append(ALL_OVERJOYED_RESPONSES[randi_range(0,ALL_OVERJOYED_RESPONSES.size()-1)])
	characterResponsesLabel.text = "Stress Response: " + responses[0] + "\nOverjoyed Response: " + responses[1]
	
	
func rollCharacter():
	rollName()
	rollAttributes()
	rollTraits()
	rollResponses()
	
func _on_edit_name_button_down():
	rollCharacter()

func _on_re_roll_button_down():
	rollCharacter()
