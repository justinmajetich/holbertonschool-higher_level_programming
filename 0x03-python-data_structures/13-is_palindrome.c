#include "lists.h"
int recursive_check(listint_t **left, listint_t *right);
/**
 * is_palindrome - check if a singly-linked list palindromic
 * @head: list head
 *
 * Return: 1 if palindromic, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head)) /* if list is empty */
		return (1);

	if (recursive_check(head, *head))
		return (1);
	else
		return (0);
}
/**
 * recursive_check - check if list is palindromic
 * @left: left pointer
 * @right: right pointer
 *
 * Return: 1 if node values match, 0 if they don't
 */
int recursive_check(listint_t **left, listint_t *right)
{
	int is_pal = 0;

	if (right) /* recurse until right pointer is NULL */
		is_pal = recursive_check(left, right->next);
	else
		return (1);

	if (is_pal == 1) /* if last values matched */
		if ((*left)->n == right->n) /* compare current values */
		{
			*left = (*left)->next; /* shift left pointer right */
			return (1);
		}
	return (0);
}
