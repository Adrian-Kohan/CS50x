#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!%i %i\n", score1, score2);
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!%i %i\n", score1, score2);
    }
    else
    {
        printf("Tie!%i %i\n", score1, score2);
    }
}

int compute_score(string word)
{
    //Compute and return score for string
    int score = 0;
    int i = 0;
    int j = 0;
    int l[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int u[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    for (i = 0 , j = 0; i < 26 && j < strlen(word);  i++&& j++ )
    {
        u[i] = l[i];
        l[i] = POINTS[i];

        do
        {
            word[j] = u[i];
        }
        while (false);

        score = score + word[j];

    }
    return score;
}