#include "lists.h"

/**
 * free_dlistint - frees a dlistint_t list
 *
 * @head: pointer to distint_t
 *
 * Return: void
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	while (head)
	{
		tmp = head;
		head = head->next;
		free(tmp);
	}
}
