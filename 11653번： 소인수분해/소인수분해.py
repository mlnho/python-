#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11653                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: 1104minho <boj.kr/u/1104minho>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11653                          #+#        #+#      #+#     #
#    Solved: 2024/09/20 21:26:46 by 1104minho     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())
K = 2

while (N!=1):
    if N % K == 0:
        N = N//K
        print(K)
    else:
        K += 1
    