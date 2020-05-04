#!/usr/bin/env python3
import unittest

from pyfastocloud.fastocloud_client import FastoCloudClient


class ClientTest(unittest.TestCase):
    def test_lifetime(self):
        host = 'localhost'
        port = 0
        client = FastoCloudClient(host, port, None, None)
        self.assertEqual(client.host, host)
        self.assertEqual(client.port, port)
        self.assertFalse(client.is_active())

        res, oid = client.activate(0, '123')
        self.assertFalse(res)
        self.assertEqual(oid, None)

        res, oid = client.ping(1)
        self.assertFalse(res)
        self.assertEqual(oid, None)

        res, oid = client.prepare_service(2, '/', '/')
        self.assertFalse(res)
        self.assertEqual(oid, None)


if __name__ == '__main__':
    unittest.main()
