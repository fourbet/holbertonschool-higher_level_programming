#include "lists.h"

/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked lists
 *
 * @head: pointer to a distint_t
 * @index: const int
 *
 * Return: the nth node or NULL
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int count = 0;
	dlistint_t *current = NULL;

	current = head;
	while (current)
	{
		if (count == index)
			return (current);
		current = current->next;
		count++;
	}
	return (NULL);
}
