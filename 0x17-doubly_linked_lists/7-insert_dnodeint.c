#include "lists.h"

/**
 * insert_dnodeint_at_index - inserts a new node at a given position
 *
 * @h: pointer to a pointer to a dlistint_t
 * @idx: int
 * @n: int
 *
 * Return: the address of the new node, or NULL if it failed
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int count = 0;
	dlistint_t *current = NULL;
	dlistint_t *previous = NULL;
	dlistint_t *new = NULL;

	new = malloc(sizeof(dlistint_t));
		if (new == NULL)
			return (NULL);
	new->n = n;
	new->prev = NULL;
	new->next = NULL;
	current = *h;
	while (current)
	{
		if (count == idx)
		{
			if (idx == 0)
			{
				*h = new;
				new->next = current;
				return (new);
			}
			previous->next = new;
			new->next = current;
			new->prev = previous;
			return (new);
		}
		previous = current;
		current = current->next;
		count++;
	}
	if (idx == count)
	{
		previous->next = new;
		new->prev = previous;
	}
	return (NULL);
}
