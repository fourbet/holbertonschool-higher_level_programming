#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes a node at a given position
 *
 * @head: pointer to a pointer to a dlistint_t
 * @index: int
 *
 * Return: 1 (SUCESS), -1 (FAILLURE)
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int count = 0;
	dlistint_t *current = NULL;
	dlistint_t *previous = NULL;

	current = *head;
	if (head == NULL)
		return (1);
	while (current)
	{
		if (count == index)
		{
			if (index == 0)
			{
				*head = current->next;
				return (1);
			}
			previous->next = current->next;
			return (1);
		}
		previous = current;
		current = current->next;
		count++;
	}
	if (index == count)
	{
		previous->next = NULL;
	}
	return (-1);
}
