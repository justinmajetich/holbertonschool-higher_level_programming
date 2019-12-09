#include "lists.h"

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
