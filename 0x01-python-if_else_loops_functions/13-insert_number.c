#include "lists.h"

/**
 * insert_node - insert node into sorted list
 * @head: head of sorted list
 * @number: value to insert
 *
 * Return: address of new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = NULL, *new = NULL;

	curr = *head;
	if (!(*head) || curr->n >= number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		new->n = number;
		new->next = curr;
		*head = new;
		return (new);
	}
	while (curr)
	{
		if (curr->n <= number && (!curr->next || curr->next->n > number))
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);

			new->n = number;
			new->next = curr->next;
			curr->next = new;
			return (new);
		}
		else
			curr = curr->next;
	}
	return (NULL);
}
