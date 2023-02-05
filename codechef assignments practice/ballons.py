s = '  Username  Password  Forgot Password  New User  CodeChef is a competitive programming community  PRACTICE & LEARNCOMPETEDISCUSSOUR INITIATIVESASSOCIATE WITH USMORE  Home » Practice(Beginner) » Malvika is peculiar about color of balloons  Malvika is peculiar about color of balloons Problem Code: CHN09  Add problem to Todo list  Submit       Little Malvika is very peculiar about colors. On her birthday, her mom wanted to buy balloons for decorating the house. So she asked her about her color preferences. The sophisticated little person that Malvika is, she likes only two colors — amber and brass. Her mom bought n balloons, each of which was either amber or brass in color. You are provided this information in a string s consisting of characters "a" and "b" only, where "a" denotes that the balloon is amber, where "b" denotes it being brass colored.    When Malvika saw the balloons, she was furious with anger as she wanted all the balloons of the same color. In her anger, she painted some of the balloons with the opposite color (i.e., she painted some amber ones brass and vice versa) to make all balloons appear to be the same color. As she was very angry, it took her a lot of time to do this, but you can probably show her the right way of doing so, thereby teaching her a lesson to remain calm in difficult situations, by finding out the minimum number of balloons needed to be painted in order to make all of them the same color.    Input  The first line of input contains a single integer T, denoting the number of test cases.  The first and only line of each test case contains a string s.  Output  For each test case, output a single line containing an integer — the minimum number of flips required.  Constraints  1 ≤ T ≤ 100  1 ≤ n ≤ 100, where n denotes to the length of the string s.  Example  Input:  3  ab  bb  baaba    Output:  1  0  2  Explanation  In the first example, you can change amber to brass or brass to amber. In both the cases, both the balloons will have same colors. So, you will need to paint 1 balloon. So the answer is 1.    In the second example, As the color of all the balloons is already the same, you don"t need to paint any of them. So, the answer is 0.    All submissions for this problem are available.  Author:	admin2  Tags:	acm15chn, admin2, looping, strings  Date Added:	15-01-2016  Time Limit:	1 secs  Source Limit:	50000 Bytes  Languages:	CPP14, C, JAVA, PYP3  Submit  All Submissions  Successful Submissions  CodeChef is a competitive programming community    About CodeChef  Contact Us  CodeChef uses SPOJ © by Sphere Research Labs  In order to report copyright violations of any kind, send in an email to copyright@codechef.com    The time now is: 01:07:58 PM  Your IP: 103.10.29.87  CodeChef - A Platform for Aspiring Programmers    CodeChef was created as a platform to help programmers make it big in the world of algorithms, computer programming, and programming contests. At CodeChef we work hard to revive the geek in you by hosting a programming contest at the start of the month and two smaller programming challenges at the middle and end of the month. We also aim to have training sessions and discussions related to algorithms, binary search, technicalities like array size and the likes. Apart from providing a platform for programming competitions, CodeChef also has various algorithm tutorials and forum discussions to help those who are new to the world of computer programming.    Practice Section - A Place to hone your "Computer Programming Skills"    Try your hand at one of our many practice problems and submit your solution in the language of your choice. Our programming contest judge accepts solutions in over 55+ programming languages. Preparing for coding contests were never this much fun! Receive points, and move up through the CodeChef ranks. Use our practice section to better prepare yourself for the multiple programming challenges that take place through-out the month on CodeChef.    Compete - Monthly Programming Contests, Cook-off and Lunchtime    Here is where you can show off your computer programming skills. Take part in our 10 days long monthly coding contest and the shorter format Cook-off and Lunchtime coding contests. Put yourself up for recognition and win great prizes. Our programming contests have prizes worth up to INR 20,000 (for Indian Community), $700 (for Global Community) and lots more CodeChef goodies up for grabs.    Programming Tools    Online IDE  Upcoming Coding Contests  Contest Hosting  Problem Setting  CodeChef Tutorials  CodeChef Wiki  Practice Problems    Easy  Medium  Hard  Challenge  Peer  School  FAQ"s  Initiatives    Go for Gold  CodeChef for Schools  College Chapters  CodeChef for Business  Policy    Terms of Service  Privacy Policy  Refund Policy  Code of Conduct  Bug Bounty Program  '
for ind, val in enumerate(s):
    print(ind, val)

for ind,val in enumerate(s):
    if s[ind] == 'b' and s[ind+1] == 'a' and s[ind+2] == 'l' and s[ind+3] == 'l':
        print('Found ball at position: ', ind)




# tests = int(input())


# for i in range(tests):
#     user_input = str(input())
#     # # my_list = []
#     # # my_list[:] = user_input
#     # # print(my_list)
#     # d = my_list.count('a')
#     # e =my_list.count('b')
#     d = user_input.count('a')
#     e= user_input.count('b')
#     print(d)
#     print(e)
#     if d<e :
#         for (i,ind) in user_input:
#             i = 'a' if i is 'a' else i#new_list= user_input.replace('a','b')
#         print(new_list)
#         print(d-1)
#         break
#     else:
#        for i in user_input:
#             new_list= user_input.replace('b','a')
#     print(new_list)
#     print(e-1)
#     break

        

    