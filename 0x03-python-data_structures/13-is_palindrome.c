#include "lists.h"
/**
 * is_palindrome - check if a singly-linked list palindromic
 * @head: list head
 *
 * Return: 1 if palindromic, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *left = NULL, *right = NULL;
	size_t len = 0, i, loff, roff; /* length and offsets */

	if (!head || !(*head))
		return (1);

	/* send right pointer to end of list */
	left = right = *head;
	while (right->next)
	{
		right = right->next;
		len++;
	}
	if (left->n == right->n)
	{
		for (roff = loff = 1; len > (loff + roff); loff++, roff++)
		{
			left = left->next;
			for (right = left, i = 0; i < (len - (loff + roff)); i++)
				right = right->next;
			if (left->n != right->n) /* if values don't match */
				return (0);
		}
	}
	else
		return (0);
	return (1);
}
