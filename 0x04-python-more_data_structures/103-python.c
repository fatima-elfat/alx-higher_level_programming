#include "Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0, i, len2;
	char *s;
	PyBytesObject *py_c = (PyBytesObject *) p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_c))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		len = PyBytes_Size(p);
		printf("  size: %ld\n", len);
		printf("  trying string: %s\n", py_c->ob_sval);
		s = py_c->ob_sval;
		len2 = len + 1;
		if (len2 >= 10)
			len2 = 10;
		printf("  first %ld bytes: ", len2);
		for (i = 0; i < len2 - 1; ++i)
			printf("%02x ", (unsigned char) s[i]);
		printf("%02x\n", (unsigned char) s[i]);
	}
}
void print_python_list(PyObject *p)
{
	Py_ssize_t  len, i;
	PyListObject *py_c = (PyListObject *) p;
	PyObject *it;

	len = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", py_c->allocated);
	for (i = 0; i < len; ++i)
	{
		/*it = PyList_GET_ITEM(p, i);*/
		it = py_c->ob_item[i];
		printf("Element %ld: %s\n", i, it->ob_type->tp_name);
		if (PyBytes_Check(it))
			print_python_bytes(it);
	}
}
