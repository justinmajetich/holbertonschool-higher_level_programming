#include "lists.h"

/**
 * check_cycle - check for cycle in linked list
 * @list: list to check
 *
 * Return: 1 if cycle detected, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow; /* pointers to traverse list */

	slow = list->next;
	fast = list->next->next;

	while (slow && fast) /* traverse list till NULL */
	{
		if (slow == fast) /* if pointers meet */
			return (1); /* cycle detected */

		slow = slow->next; /* traverse list at diff speeds */
		fast = fast->next->next;
	}
	return (0); /* no cycle detected */
}
