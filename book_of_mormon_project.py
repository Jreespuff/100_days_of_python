import random


quotes = {"1 Nephi 11:7" : 
          "And I said unto him: I know that he loveth his children; nevertheless, I do not know the meaning of all things.",
          "1 Nephi 1:20" : 
          "“But behold, I, Nephi, will show unto you that the tender mercies of the Lord are over all those whom he hath chosen, because of their faith, to make them mighty even unto the power of deliverance.”",
          "1 Nephi 20:10" :
          "“For, behold, I have refined thee, I have chosen thee in the furnace of affliction.”",
          "1 Nephi 21:13" :
          "“Sing, O heavens; and be joyful, O earth; for the feet of those who are in the east shall be established; and break forth into singing, O mountains; for they shall be smitten no more; for the Lord hath comforted his people, and will have mercy upon his afflicted.”",
          "1 Nephi 3:7" :
          "“And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them.”",
          "1 Nephi 9:6" :
          "“But the Lord knoweth all things from the beginning; wherefore, he prepareth a way to accomplish all his works among the children of men; for behold, he hath all power unto the fulfilling of all his words. And thus it is. Amen.”",
          "2 Nephi 26:28" : 
          "“Behold, hath the Lord commanded any that they should not partake of his goodness? Behold I say unto you, Nay; but all men are privileged the one like unto the other, and none are forbidden.”",
          " 2 Nephi 2:2" :
          "“And now, Jacob, I speak unto you: Thou art my first-born in the days of my tribulation in the wilderness. And behold, in thy childhood thou hast suffered afflictions and much sorrow, because of the rudeness of thy brethren.”",
          "2 Nephi 2:1-2" :
          "“Nevertheless, Jacob, my first-born in the wilderness, thou knowest the greatness of God; and he shall consecrate thine afflictions for thy gain.”",


}

res = key, val = random.choice(list(quotes.items()))
 
# printing result
print(str(res))

