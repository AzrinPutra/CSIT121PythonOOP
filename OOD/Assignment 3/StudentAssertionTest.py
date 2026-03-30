from A3shannon import Analytic
from datetime import datetime

def test_get_directors():
	expected = set(['Charles', 'Don', 'Eric','Bob'])
	analytic = Analytic("MovieSales.csv")
	r = set(analytic.get_directors())
	assert expected == r, "test_get_directors failed"
	print("test_get_directors() passed")

def test_get_geners():
	expected = set(['Comedy', 'Action', 'Drama'])
	analytic = Analytic("MovieSales.csv")
	r = set(analytic.get_genres())
	assert expected == r, "test_get_geners failed"
	print("test_get_geners() passed")

def test_count():
	analytic = Analytic("MovieSales.csv")
	assert analytic.count == 20, "test_count 1 failed"
	analytic = Analytic("MovieSales_Errors.csv")
	assert analytic.count == 3, "test_count 2 failed"
	print("test_count() passed")

def test_return_data():
	expected = [{'title': 'Title_1', 'genre': 'Action', 'year_of_release': 2022, 'director': 'Bob', 'studio': 'Studio_A', 'global_sales': 7.18, 'critic_score': 13, 'rating': 'PG-13'}]
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(title=["Title_1"])
	assert compare_dict_lists(expected,r), "test_return_data failed"
	expected = [{'title': 'Title_2', 'genre': 'Action', 'year_of_release': 2022, 'director': 'Charles', 'studio': 'Studio_A', 'global_sales': 2.57, 'critic_score': 76, 'rating': 'PG-13'}, {'title': 'Title_3', 'genre': 'Action', 'year_of_release': 2022, 'director': 'Don', 'studio': 'Studio_A', 'global_sales': 3.59, 'critic_score': 39, 'rating': 'PG-13'}]
	r = analytic.match(title=["Title_2","Title_3"])
	assert compare_dict_lists(expected,r), "test_return_data failed"
	print("test_return_data() passed")

def test_match_title():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(title=["Title_1","Title_2","Title_3","Title_A"])
	assert len(r) == 3, "test match title 1 failed"
	r = analytic.match(title=["Title_B"])
	assert len(r) == 0, "test match title 2 failed"
	print("test_match_title() passed")

def test_match_genre():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(genre=["Action"])
	assert len(r) == 5, "test match genre 1 failed"
	r = analytic.match(genre=["Action","Comedy"])
	assert len(r) == 14, "test match genre 2 failed"
	r = analytic.match(genre=["None"])
	assert len(r) == 0, "test match genre 3 failed"
	print("test_match_genre() passed")

def test_match_year_released():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(year_of_release=[2020,2022])
	assert len(r)==11,"test match year_released 1 failed"
	r = analytic.match(year_of_release=[2022,2022])
	assert len(r)==4,"test match year_released 2 failed"
	r = analytic.match(year_of_release=[2000,2010])
	assert len(r)==0,"test match year_released 3 failed"
	print("test_match_year_released() passed")


def test_match_director():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(director=["Bob"])
	assert len(r)==8, "test_match_director 1 failed"
	r = analytic.match(director=["Bob","Eric"])
	assert len(r)==10, "test_match_director 2 failed"
	r = analytic.match(director=["Bob","Eric","None"])
	assert len(r)==10, "test_match_director 3 failed"
	r = analytic.match(director=["None"])
	assert len(r)==0, "test_match_director 4 failed"
	print("test_match_director() passed")

def test_match_studio():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(studio=["Studio_A"])
	assert len(r)==10, "test_match_studio 1 failed"
	r = analytic.match(studio=["Studio_A","Studio_B"])
	assert len(r)==20, "test_match_studio 2 failed"
	print("test_match_studio() passed")

def test_match_global_sales():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(global_sales=[0.1,0.58])
	assert len(r)==1, "test_match_global_sales 1 failed"
	r = analytic.match(global_sales=[9,10])
	assert len(r)==3, "test_match_global_sales 2 failed"
	r = analytic.match(global_sales=[20,30])
	assert len(r)==0, "test_match_global_sales 3 failed"
	print("test_match_global_sales() passed")
	
def test_match_critic_score():
	analytic = Analytic("MovieSales.csv")
	r = analytic.match(critic_score=[0,100])
	assert len(r)==20, "test_match_critic_score 1 failed"
	r = analytic.match(critic_score=[10,20])
	assert len(r)==5, "test_match_critic_score 2 failed"
	r = analytic.match(critic_score=[99,100])
	assert len(r)==0, "test_match_critic_score 3 failed"
	print("test_match_critic_score() passed")

def test_match_rating():
	analytic = Analytic("MovieSales.csv")
	r =  analytic.match(rating=["PG-13"])
	assert len(r)==4, "test_match_rating 1 failed"
	r =  analytic.match(rating=["PG-13","PG"])
	assert len(r)==9, "test_match_rating 2 failed"
	r =  analytic.match(rating=["PG-13","PG","None"])
	assert len(r)==9, "test_match_rating 3 failed"
	r =  analytic.match(rating=["None"])
	assert len(r)==0, "test_match_rating 4 failed"
	print("test_match_rating() passed")

def test_match_genre_year_release():
	analytic = Analytic("MovieSales.csv")
	r =  analytic.match(genre=["Comedy"],year_of_release=[2020,2020])
	assert len(r)==3, "test_match_genre_year_release 1 failed"
	r =  analytic.match(genre=["Comedy","Action"],year_of_release=[2020,2022])
	assert len(r)==10, "test_match_genre_year_release 2 failed"
	print("test_match_genre_year_release() passed")


def compare_dict_lists(list1, list2):
    """
    Compare two lists of dictionaries to check if they contain the same dictionaries with the same data.
    Order does not matter.
    """
    # Convert each dict to a frozenset of its items for hashable comparison
    set1 = {frozenset(d.items()) for d in list1}
    set2 = {frozenset(d.items()) for d in list2}
    
    return set1 == set2

def test():
	try:
		test_get_directors()
		test_get_geners()
		test_count()
		test_return_data()
		test_match_title()
		test_match_genre()
		test_match_year_released()
		test_match_director()
		test_match_studio()
		test_match_global_sales()
		test_match_critic_score()
		test_match_rating()
		test_match_genre_year_release()
		#continue your testing adventure below.....
	except Exception as ex:
		print(ex)

def error_test():
	#this generate the sample errors.txt
	Analytic("MovieSales_Errors.csv")

if __name__ == "__main__":
	test()
	error_test()
