#include "lists.h"
listint_t *add_nodeint(listint_t **head, const int n);
int check_cycle(listint_t *list);
/**
 * is_palindrome - check if a singly-linked list palindromic
 * @head: list head
 *
 * Return: 1 if palindromic, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev = NULL, *temp = NULL, *rtemp = NULL;
	size_t list_len = 0;

	if (!head || !(*head))
		return (1);

	if (check_cycle(*head)) /* if list has cycle */
		return (0);

	/* create list in reverse to compare against */
	temp = *head;
	while (temp)
	{
		add_nodeint(&rev, temp->n);
		temp = temp->next;
		list_len++;
	}
	/* compare list to reverse copy */
	temp = *head;
	rtemp = rev;
	while (temp)
	{
		if (temp->n != rtemp->n)
		{
			free_listint(rev);
			return (0);
		}
		temp = temp->next;
		rtemp = rtemp->next;
	}
	free_listint(rev);
	return (1);
}
/**
 * add_nodeint - add new node to beginning of list
 * @head: pointer to list head
 * @n: value to initialize in new node
 *
 * Return: address of new node on Success, NULL on Fail
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t node; /* new node */
	listint_t *new = &node; /* pointer to new node */

	/* check for NULL head */
	if (!head)
		return (NULL);

	/* allocate for new node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	/* initialize new node */
	new->n = n;
	new->next = *head; /* point new head to old head */

	/* assign head pointer to new head */
	*head = new;

	return (new);
}
/**
 * check_cycle - check for cycle in linked list
 * @list: list to check
 *
 * Return: 1 if cycle detected, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast; /* pointer to traverse list */

	if (list && list->next)
		fast = list->next;
	else
		return (0);

	while (list && fast) /* traverse list till NULL */
	{
		if (list == fast) /* if pointers meet */
			return (1); /* cycle detected */

		list = list->next; /* traverse list at diff speeds */

		if (fast->next)
			fast = fast->next;
		else
			return (0);

		if (fast->next)
			fast = fast->next;
		else
			return (0);
	}
	return (0); /* no cycle detected */
}
