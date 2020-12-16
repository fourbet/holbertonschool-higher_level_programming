#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: pointer to pointer to a listint
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *last;
	int length = 0;
	int n = 2;
	int count = 0;

	current = *head;
	last = *head;
	if (*head == NULL)
		return (0);
	while (last->next)
	{
		length++;
		last = last->next;
	}
	length++;
	if (length == 1)
		return (0);
	while (current)
	{
		if (current == last)
			return (1);
		if (current->n == last->n)
		{
			current = current->next;
			count = length - n;
			last = *head;
			while (count > 0)
			{
				last = last->next;
				count--;
			}
			n++;
		}
		else
			return (0);
	}
	return (1);
}

